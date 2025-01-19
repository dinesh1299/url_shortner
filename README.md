
## Installation

1. Clone the repository
   cd url_shortener

2. Set Up Virtual Environment
   python -m venv env
   env\Scripts\activate

3. Install Dependencies
   pip install -r requirements.txt

4. Initialize Database
   python manage.py makemigrations
   python manage.py migrate

5. Run the Development Server
   python manage.py runserver


## Usage

### Shorten a URL
1. Open the application in your browser: http://127.0.0.1:8000
2. Enter the long URL you want to shorten.
3. Specify the expiration time in hours.
4. Click the Submit button to generate a shortened URL.

### Redirect to Original URL
1. Copy the shortened URL.
2. Paste it in your browser to be redirected to the original URL.

### View URL List
1. Visit http://127.0.0.1:8000/json/url/.
2. View the list of Original url and Short url.

### View Analytics
1. Visit http://127.0.0.1:8000/analytics/<short_url>/.
2. View the list of access logs, timestamps and IP addresses.
