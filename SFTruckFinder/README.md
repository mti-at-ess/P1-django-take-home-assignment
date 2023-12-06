# San Francisco Truck Finder
San Francisco truck finder is an initial application to find nearest trucks for san francisco people. 

## 🕹️ Approach
At first, as the information for all trucks was already provided, I thought of having them in databases instead of reading file on every endpoint call. Which is why i had to introduce a commands in the main application to populate the database based on the CSV. Its not perfect, but it is optimised according to the current provided data.

Nextly in order to suggest back the truck suggestion, I went with a simpler approach of using haversine distance algorithm to get the distance between all points and the location provided and suggest the nearest approved food trucks. 

## 🚀 Installation / Setup
- Install **python v3.9.6**
- Run ```pip install -r requirements.txt``` from root directory.
- For migrations, run ```cd SFTruckFinder && python manage.py migrate``` from root directory.
- Start the server by ```cd SFTruckFinder && python manage.py runserver``` from root directory.

## 📝 Usage
The truck finder application is exposed at `/foodtrucks` subdomain. In order to interact with it use the below URL:
- **Trucks List**: _GET_ `/fetch_trucks?latitude={latitude_value}&longitude={longitude_value}`
