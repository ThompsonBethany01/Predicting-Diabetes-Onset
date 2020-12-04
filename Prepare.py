import pandas as pd

def prep_df(df):

    '''
    Preps a single df on diabetes data. Imputes 0 values that can not be 0's with
    the feature mean. Creates features based on binning. Returns the df.
    '''

    # Imputing 0 values that cannot be 0 (i.e. BMI) with mean
    # BMI
    bmi_mean = df.BMI.mean()
    df.BMI = df.BMI.replace(0,bmi_mean)

    # Glucose
    glucose_mean = df.Glucose.mean()
    df.Glucose = df.Glucose.replace(0,glucose_mean)

    # Blood Pressure
    bp_mean = df.BloodPressure.mean()
    df.BMI = df.BMI.replace(0,bmi_mean)

    # Feature Engineering, binning features

    # 1 = 'early_20s', 2 = 'late_20s', 3 = '30s', 4 = '40s_to_80s']
    # (20.999, 24.0] < (24.0, 29.0] < (29.0, 41.0] < (41.0, 81.0]
    df['age_bins'] = pd.qcut(df.Age, 4, labels=[1,2,3,4])

    # 1 = low, 2 = medium, 3 = high
    # (-0.001, 29.0] < (29.0, 34.867] < (34.867, 67.1]
    df['bmi_bins'] = pd.qcut(df.BMI, 3, labels=[1,2,3])

    # 1 = low, 2 = medium, 3 = high
    # (-0.001, 66.0] < (66.0, 76.0] < (76.0, 122.0]
    df['bp_bins'] = pd.qcut(df.BloodPressure, 3, labels=[1,2,3])

    # creating column for patient with both high bp and bmi
    df['high_bmi_bp'] = (df.bmi_bins == 2) | (df.bmi_bins == 3) & (df.bp_bins == 3)

    return df

def split_df(df):

    '''
    Splits df into train, validate, and test - 70%, 20%, 10% respectively.
    Prints out the percentage shape and row/column shape of the split dfs.
    Returns train, validate, test.
    '''

    # Import to use split function, can only split two at a time
    from sklearn.model_selection import train_test_split

    # First, split into train + validate together and test by itself
    # Test will be %10 of the data, train + validate is %70 for now
    # Set random_state so we can reproduce the same 'random' data
    train_validate, test = train_test_split(df, test_size = .10, random_state = 123)

    # Second, we split train + validate into their seperate variables
    # Train will be %70 of the data, Validate will be %20 of the data
    train, validate = train_test_split(train_validate, test_size = .22, random_state = 123)

    # These two print functions allow us to ensure the date is properly split
    # Will print the shape of each variable when running the function
    print("train shape: ", train.shape, ", validate shape: ", validate.shape, ", test shape: ", test.shape)

    # Will print the shape of eachvariable as a percentage of the total data set
    # Varialbe to hold the sum of all rows (total observations in the data)
    total = df.count()[0]
    print("\ntrain percent: ", round(((train.shape[0])/total),2) * 100, 
        ", validate percent: ", round(((validate.shape[0])/total),2) * 100, 
        ", test percent: ", round(((test.shape[0])/total),2) * 100)

    return train, validate, test

def scale_dfs(train, validate, test, predict):

    '''
    Scales a df based on MinMaxScaler. Needs three dfs, train, validate, teset.
    Fits the scaler object to train only, ptransforms on all 3. Returns three
    dfs scaled.
    '''

    import sklearn.preprocessing

    # removing predictive feature
    X_train = train.drop(predict, axis=1)
    X_validate = validate.drop(predict, axis=1)
    X_test = test.drop(predict, axis=1)

    # create object
    scaler = sklearn.preprocessing.MinMaxScaler()

    # Note that we only call .fit with the training data,
    # but we use .transform to apply the scaling to all the data splits.
    scaler.fit(X_train)

    X_train_scaled = scaler.transform(X_train)
    X_validate_scaled = scaler.transform(X_validate)
    X_test_scaled = scaler.transform(X_test)

    # converting scaled array baack to df
    X_train_scaled = pd.DataFrame(X_train_scaled)
    X_train_scaled.index = X_train.index
    X_train_scaled.columns = X_train.columns

    X_validate_scaled = pd.DataFrame(X_validate_scaled)
    X_validate_scaled.index = X_validate.index
    X_validate_scaled.columns = X_validate.columns

    X_test_scaled = pd.DataFrame(X_test_scaled)
    X_test_scaled.index = X_test.index
    X_test_scaled.columns = X_test.columns

    return X_train_scaled, X_validate_scaled, X_test_scaled

def create_clusters(X_train_scaled, X_validate_scaled, X_test_scaled, train, validate, test, features, n, columns, cluster):
    '''
    Create clusters based on features specified. n is amount of groupds within the cluster.
    columns is the name of the dummy variable columns created after making the cluster.
    cluster is the name of the cluster, based on features used to create it. Best when
    used on scaled dfs, function is for split train, validate, test dfs.
    '''
    from sklearn.cluster import KMeans

    X = X_train_scaled[features]
    Y = X_validate_scaled[features]
    Z = X_test_scaled[features]
    
    # create object with 4 clusters
    kmeans = KMeans(n_clusters=n)

    # fit to the features chosen
    kmeans.fit(X)

    # predict clusters 
    kmeans.predict(X)

    # add column in unscaled df of these cluster predictions
    train[cluster] = kmeans.predict(X)
    validate[cluster] = kmeans.predict(Y)
    test[cluster] = kmeans.predict(Z)

    dummies = pd.get_dummies(train[cluster])
    dummies.columns = columns

    dummies2 = pd.get_dummies(validate[cluster])
    dummies2.columns = columns

    dummies3 = pd.get_dummies(test[cluster])
    dummies3.columns = columns

    # add cluster dummy variables to scaled df
    train = pd.concat([train,dummies], axis=1)
    validate = pd.concat([validate,dummies2], axis=1)
    test = pd.concat([test,dummies3], axis=1)

    # add column in scaled df of these cluster predictions
    X_train_scaled[cluster] = kmeans.predict(X)
    X_validate_scaled[cluster] = kmeans.predict(Y)
    X_test_scaled[cluster] = kmeans.predict(Z)

    dummies = pd.get_dummies(X_train_scaled[cluster])
    dummies.columns = columns

    dummies2 = pd.get_dummies(X_validate_scaled[cluster])
    dummies2.columns = columns

    dummies3 = pd.get_dummies(X_test_scaled[cluster])
    dummies3.columns = columns

    # add cluster dummy variables to scaled df
    X_train_scaled = pd.concat([X_train_scaled,dummies], axis=1)
    X_validate_scaled = pd.concat([X_validate_scaled,dummies2], axis=1)
    X_test_scaled = pd.concat([X_test_scaled,dummies3], axis=1)

    return X_train_scaled, X_validate_scaled, X_test_scaled, train, validate, test