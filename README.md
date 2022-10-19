# Documentation

Start the application from your directory:

    docker-compose up
   
<hr>
   
Then you can send GET requset

Example

    http://127.0.0.2:5000/api/rates?from=USD&to=RUB&value=1
    
Result will be in JSON:

![image](https://user-images.githubusercontent.com/59223504/196721340-37fe851f-6de8-46ed-979f-404a3c923987.png)

## Get your API key

1. Visit https://fixer.io/
2. Click GET FREE API KEY

![image](https://user-images.githubusercontent.com/59223504/196722080-49ec11ab-e754-4271-993b-7eb7c6f2aea6.png)

3. Set your api key as environment variable

        set API_KEY = 'your_api_key_here'

