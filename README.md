# PornRecommendationBackend

### Before we begin,
Problems:
 - Inside [app/main.py](https://github.com/daeisbae/PornRecommendationBackend/blob/main/app/main.py), I implemented pd.read_csv inside the function as I deployed the code at [Google Cloud Run](https://cloud.google.com/run/?utm_source=google&utm_medium=cpc&utm_campaign=japac-AU-all-en-dr-bkws-all-pkws-trial-e-dr-1009882&utm_content=text-ad-none-none-DEV_c-CRE_529515645060-ADGP_Hybrid%20%7C%20BKWS%20-%20EXA%20%7C%20Txt%20~%20Compute%20~%20Cloud%20Run_cloud%20run-general%20-%20Products-44225-KWID_43700060418856433-aud-970366092687%3Akwd-678836618089&userloc_9001527-network_g&utm_term=KW_google%20cloud%20run&gclid=CjwKCAiAtouOBhA6EiwA2nLKHw96a8vxtbKUdjVmuYGGs96Ww1R-FiyFsrpfC-n0yRY2Zc0gvkQp5hoCU2IQAvD_BwE&gclsrc=aw.ds) which is a serverless computing service.
 - Serverless computing awakes the code/functions when it is needed which means it will initialize the code/function everytime (Code will restart everytime).
 - In case of cloud computing like [AWS EC2](https://www.google.com/aclk?sa=L&ai=DChcSEwjphPHBsfn0AhU4H60GHauMDcAYABACGgJwdg&ae=2&sig=AOD64_2eCt0JlJRM_pTSjqM4OLchBun0wA&q&adurl&ved=2ahUKEwjziOjBsfn0AhVEKn0KHX-kC3AQ0Qx6BAgDEAE), placing pd.read_csv outside the function would be better solution, saving a lot of resources. However in serverless computing, putting pd.read_csv outside a funcion is not ideal as it will repeat pd.read_csv everytime even when reading the csv file is not needed.


### How to install
* Prerequisite: Install [Docker](https://docs.docker.com/get-docker/)
1. Change CommandLine directory to this project path
```CMD
cd ~/PornRecommendationBackend
```
2. Build docker image: Type this code in CommandLine which is routed to this project(folder) path
```CMD
docker build -t porn-backend:1.0 .
```
3. Run
```CMD
docker run -d -p 5000:5000 porn-backend:1.0
```
4. Test if it is working: visit http://localhost:5000/ to check if it is responding `hello world`. If it does, it is working properly!

### How to make a requests?
if you have installed it correctedly,<br>
Make Json requests to get list of porn recommendation<br>
1. It should have this following parameters
- `minDuration` is the minimum duration of recommended porn in Seconds => ***Integer***<br>
- `maxDuration` is the maximum duration of recommended porn in Seconds => ***Integer***<br>
- `minViews` is the minimum views required for recommended porn => ***Integer***<br>
- `pornstars` is the list of pornstars you like  => ***List[String]***<br>
- `categories` is the list of categories you like =>  => ***List[String]***<br>

The example of Json request to /upload<br>
```json
{
  "minDuration": 0,
  "maxDuration": 1000,
  "minViews": 30,
  "pornstars": [
    "Aaliyah Love",
    "Aaron Landcaster"
  ],
  "categories": [
    "Toys",
    "Mature"
  ]
}
```
2. Make a ***POST*** requests to http://localhost:5000/upload attaching JSON that we just made<br>
