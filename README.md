# PornRecommendationBackend

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
