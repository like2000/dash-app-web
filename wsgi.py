from dash_web_app import create_app

# app.run(host='0.0.0.0', debug=True)
if __name__ == '__main__':
    app = create_app()
    app.run()
