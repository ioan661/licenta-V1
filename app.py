from website import create_app

app = create_app() 

if __name__ == '__main__': 
    app.run(host="192.168.1.101", port=3000, debug=True)