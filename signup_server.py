from signup import app

# 1. Need to open port 5000 on the server: sudo ufw allow 5000
# 2. Accept network traffic: host='0.0.0.0'
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True) 