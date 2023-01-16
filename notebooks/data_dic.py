#Create Data Frame
data_dictionary_content = {
    "Name":[
        "yards_gained",
        "quarter_seconds_remaining",
        "qtr",
        "down",
        "yardline_100",
        "ydstogo",
        "score_differential",
        "posteam",
        "defteam",
        "home_team",
        "away_team"

    ],

    "Description":[
        "Yards gained/lost in the play excluding yards gained via fumble recoveries and laterals",
        "Seconds on the clock until the quarter ends",
        "Current quater 1-4 and 5 for overtime",
        "Current down",
        "Distance to the opponents endzone in yards",
        "Yards to the next first down",
        "Score difference between offense team and the defense team",
        "Offense Team",
        "Defense Team",
        "Home Team",
        "Guest/Away Team"
    ],

    "Role":[
        "Response",
        "Predictor",
        "Predictor",
        "Predictor",
        "Predictor",
        "Predictor",
        "Predictor",
        "Predictor",
        "Predictor",
        "Predictor",
        "Predictor"
    ],

    "Type":[
        "numeric",
        "numeric",
        "numeric",
        "numeric",
        "numeric",
        "numeric",
        "numeric",
        "nominal",
        "nominal",
        "nominal",
        "nominal"     
    ],

    "Format":[
        "float64",
        "int64",
        "int64",
        "float64",
        "float64",
        "int64",
        "float64",
        "object",
        "object",
        "object",
        "object"
    ]
}