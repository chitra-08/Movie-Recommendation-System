from flask import Flask, render_template, request, redirect, url_for
import pickle
import sklearn
import pandas as pd

app = Flask(__name__)
model_CBS = pd.read_pickle("Content-Based-Movie-RS.pkl")
# file = pd.read_csv("netflix_list.csv")
# file.to_html("Movies.html")


@app.route('/')
def home():
    return render_template('Netflix Movies RS.html')

@app.route('/showMovies')
def showMovies():
    return render_template('Movies.html')

@app.route('/contentBased', methods=['GET', 'POST'])
def searchCBS():
    if request.method == 'POST':
        moviename = request.form.get('searchMovieText')
        moviename = moviename.casefold()
        
        try:
            res = model_CBS[moviename].sort_values(ascending=False)[0:11]
            movie_rs = list(res.index)

            return render_template("Netflix Movies RS.html", movie_list=movie_rs)
        except KeyError as e:
            print(
                "Sorry, we cannot find this movie in our database. Pls try providing full and correct name of the "
                "movie.")
            return render_template("Netflix Movies RS.html")

    return render_template('Netflix Movies RS.html')


if __name__ == '__main__':

    app.run(host='0.0.0.0', debug=True)
