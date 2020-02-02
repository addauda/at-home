## ZListing model
Sample JSON
```
{
	(Required)
	"id": 29, //integer
	"price": 750000, //float
	"address": "", //string
	"city": "Woodland Hills", //string
	"state": "CA", //string
	"zipcode": "91367", //string

	(Optional)
	"area_unit": "SqFt",
	"bathrooms": 3,
	"bedrooms": 4, 
	"home_size": 1479, 
	"home_type": "SingleFamily",
	"last_sold_date": "2018-06-08", //date YYYY-MM-DD
	"last_sold_price": 750000, //float
	"link": "instagram.com", //string
	"price": 750000, //float
	"property_size": 7511, //float
	"rent_price": null, //float
	"rentzestimate_amount": 3000, //float
	"rentzestimate_last_updated": "2018-08-07", //date YYYY-MM-DD
	"tax_value": 529455, //float
	"tax_year": 2017, //integer
	"year_built": 1954, //integer
	"zestimate_amount": 669384, //float
	"zestimate_last_updated": "2018-08-07", //date YYYY-MM-DD
}
```

## API Endpoints
---
- ### Creates a new listing

  | Verb | Route |
  | ----------- | ----------- |
  | **POST** | `/zlistings/`|

  **Request Body** 

    ```
  	{
  		See Zlisting JSON
  	}
  	```

  **Responses**

	- 201 CREATED 
  
    	```
    	{
    		See Zlisting JSON
    	}
    	```
	
	- 400 BAD REQUEST
    	
		You can expect to receive a list of fields and respective errors.

		Sample response
    	```
    	{
    		"address": [
                "This field is required."
            ],
			"zipcode": [
                "This field is required."
            ]
    	}
    	```

---

- ### Retrieve all listings or a particular listing

  | Verb | Route |
  | ----------- | ----------- |
  | **GET** | `/zlistings/`|
  | **GET** | `/zlistings/{id}/`|

  **Request Body** - None

  **Responses**

	- 200 OK
  
		Response data is paginated with maximum page size of 50 listings. Use url in `next` field to retrieve next page. 

		Sample response
    	```
    	{
    		"count": 448
        	"next": "http://127.0.0.1:8000/zlistings/?limit=50&offset=50",
			"previous": null,
			"results": [
				{ See Zlisting JSON }, { } ...
			]
		}
  		```

	- 404 NOT FOUND

---

- ### Update a listing 

  | Verb | Route |
  | ----------- | ----------- |
  | **PUT** | `/zlistings/{id}/`

  **Request Body** 

	```
	{
		See Zlisting JSON
	}
	```
  **Responses**

    - 200 OK
    	```
		{
			See Zlisting JSON
		}
		```
	- 404 NOT FOUND

---

- ### Delete a listing

  | Verb | Route |
  | ----------- | ----------- |
  | **DELETE** | `/zlistings/{id}/`|

  **Request Body** - None

  **Responses**

  - 204 NO CONTENT
  - 404 NOT FOUND