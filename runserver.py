from iamjeremiah import app
import os
os.system("/usr/local/Cellar/mongodb/2.4.6/mongod &")
app.run(debug=True, host='0.0.0.0',port=80)
