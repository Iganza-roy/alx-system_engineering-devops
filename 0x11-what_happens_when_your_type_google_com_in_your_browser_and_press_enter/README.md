# What happens when you type google.com in your browser and press Enter

This directory contains my tasks on the 0x11 project

This project was aimed at writing a blog post explaining how web browsing works. The first file, ```0-blog_post```, contains a link to my blog post for the same, and it covers the following:
- DNS request
- TCP/IP
- Firewall
- HTTPS/SSL
- Load-balancer
- Web server
- Application server
- Database
  
The second file, ```1-what_happen_when_diagram```, contains a link to a schema to the blog post illustrating the flow of the request created when you type ```https://www.google.com``` in your browser and press ```Enter```.  The diagram shows:

- DNS resolution
- that the request hitting server IP on the appropriate port
- that the traffic is encrypted
- that the traffic goes through a firewall
- that the request is distributed via a load balancer
- that the web server answers the request by serving a web page
- that the application server generates the web page
- that the application server request data from the database

<img src="https://www.computerworld.com/wp-content/uploads/2024/03/internet_web_browser_https_url_address_bar_by_cybraingettyimages-1174404944_2400x1600-100854834-orig.jpg?resize=1536%2C1024&quality=50&strip=all">
