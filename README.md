## Test-Shop
### Prerequisites

* python **3.10**
* pip


### Installation

1. Clone the repo.
   ```sh
   $ https://github.com/WaveOfCoding/test-shop.git
   ```
2. Activate virtual environment.
   ```sh
   $ cd shop
   $ python3.10 -m venv venv
   $ source venv/bin/activate
3. Install requirements.
    ```sh
   (venv) $ pip install -r requirements.txt
   ```
4. DB Migrations.
   ```sh
   python manage.py makemigrations
   python manage.py migrate
   ```
5. Run application.
   ```sh
   python manage.py runserver
   ```