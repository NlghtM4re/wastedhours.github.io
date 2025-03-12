from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        try:
            hours_wasted = float(request.form['hours_wasted'])
            minutes_wasted = hours_wasted * 60

            books = hours_wasted / 4.8
            movies = hours_wasted / 2
            walk = minutes_wasted / 12.25
            skills = hours_wasted / 20
            ride = minutes_wasted / 5
            languages = hours_wasted / 400
            animes = minutes_wasted / 20

            if hours_wasted < 0:
                result = "You can't waste negative hours"
            elif minutes_wasted < 5:
                result = "You almost wasted no hours"
            else:
                result = [
                    f"In the {hours_wasted:.0f} wasted hours you could have:",
                    f"- ridden {ride:.1f} km",
                ]
                if minutes_wasted >= 12.25:
                    result.append(f"- walked {walk:.1f} km")
                    if minutes_wasted >= 20:
                        result.append(f"- watched {animes:.0f} episodes of anime")
                        if hours_wasted >= 2:
                            result.append(f"- read {books:.0f} books")
                            if hours_wasted >= 4.8:
                                result.append(f"- watched {movies:.0f} movies")
                                if hours_wasted >= 20:
                                    result.append(f"- learned {skills:.0f} new skills")
                                    if hours_wasted >= 400:
                                        result.append(f"- learned {languages:.0f} new languages")
        except ValueError:
            result = "Please enter a valid number."
    
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
