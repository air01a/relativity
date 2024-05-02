# relativity
Few general relativity test
```
pip install -r requirements.txt
```

## Black hole deformation
Raytracing for blackhole lens effect approximation (schwarschild metric approximation)
```
python blackhole.py
```
![alt text](doc/blackhole.png)
![alt text](doc/defelection.png)

## Mercury trajectory
Calculate python trajectory using relativity geodesic
```
python mercury.py
```
![alt text](doc/mercury_1.png) 
![alt text](doc/mercury_2.png)


## Light geodesic
simulate light trajectory
```
python photo_geodesic.py
```
![alt text](doc/light_geodesic.png)

## Geodesic for any curved surface
Draw geodesics for given curved surface equation and initial condition
 - calculate metric from surface equation
 - calculate christoffel symbols
 - integrator to solve geodesic equation

```
python metric.py
```
![alt text](doc/geo1.png)

## Mercury precession
Calculate precession for mercury (newtonian + relativity) and draw orbits 
```
python precession.py
```
![alt text](doc/precession.png)