from flask import Flask
from flask import render_template
from wfapi import Workflowy


app = Flask(__name__)


@app.route("/")
@app.route('/<share>')
def hello(share="Ast9674jor"):
    wf = Workflowy(share)
    return render_template(
        'index-new.html',
        nodes=[c for c in wf.root if not c.completed_at],
        name=wf.root.name,
        description=wf.root.description,
        github_user="0atman"
    )

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
