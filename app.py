# importing the necessary dependencies
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
import pickle

app = Flask(__name__)  # initializing a flask app


@app.route('/', methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    return render_template("index.html")


@app.route('/predict', methods=['POST', 'GET'])  # route to show the predictions in a web UI
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            rate_marriage = float(request.form['rate_marriage'])
            yrs_married = float(request.form['yrs_married'])
            educ = float(request.form['educ'])
            religious = float(request.form['religious'])
            occupation = float(request.form['occupation'])
            occupation_husb = float(request.form['occupation_husb'])

            occupation_self_1 = 0
            occupation_self_2 = 0
            occupation_self_3 = 0
            occupation_self_4 = 0
            occupation_self_5 = 0
            occupation_self_6 = 0
            if occupation == 1:
                occupation_self_1 = 0
            elif occupation == 2:
                occupation_self_2 = 1
            elif occupation == 3:
                occupation_self_3 = 1
            elif occupation == 4:
                occupation_self_4 = 1
            elif occupation == 5:
                occupation_self_5 = 1
            elif occupation == 6:
                occupation_self_6 = 1

            occupation_husb_1 = 0
            occupation_husb_2 = 0
            occupation_husb_3 = 0
            occupation_husb_4 = 0
            occupation_husb_5 = 0
            occupation_husb_6 = 0
            if occupation_husb == 1:
                occupation_husb_1 = 0
            elif occupation_husb == 2:
                occupation_husb_2 = 1
            elif occupation_husb == 3:
                occupation_husb_3 = 1
            elif occupation_husb == 4:
                occupation_husb_4 = 1
            elif occupation_husb == 5:
                occupation_husb_5 = 1
            elif occupation_husb == 6:
                occupation_husb_6 = 1

            filename = 'woman_affair_model.pickle'
            loaded_model = pickle.load(open(filename, 'rb'))  # loading the model file from the storage

            # predictions using the loaded model file
            prediction = loaded_model.predict(
                [[occupation_self_2, occupation_self_3, occupation_self_4, occupation_self_5, occupation_self_6,
                  occupation_husb_2, occupation_husb_3, occupation_husb_4, occupation_husb_5, occupation_husb_6,
                  rate_marriage, yrs_married, religious, educ]])
            print('prediction is', prediction)
            # showing the prediction results in a UI
            return render_template('index.html', hasValues=int(prediction[0]) > -1, prediction=int(prediction[0]))
        except Exception as e:
            print('The Exception message is: ', e)

            return 'something is wrong'
    # return render_template('results.html')
    else:
        return render_template('index.html')


if __name__ == "__main__":
    # app.run(host='127.0.0.1', port=8001, debug=True)
    app.run(debug=True)  # running the app
