from flask import request, Flask, Response, render_template
from filesyncer import FileSyncer

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/sync_status/<ip_addr>", methods=['GET', 'POST'])
def sync_status(ip_addr):
    if request.method == 'GET':
        data = request.args
        print 'request.args={}'.format(request.args)
    else:
        data = request.form
        print 'request.form={}'.format(request.form)
    filesyncer = FileSyncer(
                          ip_addr,
                          data['username'],
                          data['password']
                         )
    sync_status_json = filesyncer.get_sync_status()
    resp = Response(response=sync_status_json,
                    status=200,
                    mimetype="application/json")

    return resp

if __name__ == "__main__":
    app.run(debug=True)
