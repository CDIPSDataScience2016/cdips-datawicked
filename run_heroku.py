from app import app
import os

port = os.environ.get('PORT', 5000)
app.run(host='0.0.0.0', port=port, debug=True)
