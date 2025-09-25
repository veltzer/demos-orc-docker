# Run `nginx` and open port

* Bring over the nginx image from docker hub

```bash
$ docker pull nginx
```

* Now run nginx while opening a port to work with it:

```bash
$ docker run -d -p 8080:80 ngnix
```

* Now access nginx to see that it is running and accessible:

```bash
$ curl localhost:8080
```

* (If possible) access your nginx with your browser.
Open your browser at http://[your_ip]:8080
