from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)  # enables debug mode (turn off when finished proj.)

