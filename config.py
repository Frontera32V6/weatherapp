#conifg przygotowuje nam nasz program przed rozpoczęciem, czyli pobiera odpowiednie dane ze zmiennych systemowych (między innymi...)
import os #słuzy do kontaktu python ze zmiennymi systemowymi
from dotenv import load_dotenv #importowanie nie całej biblioteki a tylko jednej funkcji, wtedy mnie wazy

load_dotenv()
class Config: #klasy z zasady pisze się z duzej na początku
    QUERY=os.getenv('QUERY') #zmienne środowiskowe piszemy wielkimi literami
    API_KEY=os.getenv('API_KEY')