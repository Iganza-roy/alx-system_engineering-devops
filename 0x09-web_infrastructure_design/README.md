# Web infrastructure design
![logo](https://patchmanager.com/wp-content/uploads/IoT-office-1200-x-628.png)

## Overview
This project aims to design a web infrastructure that hosts a website reachable via ```www.foobar.com``` with the IP address ```8.8.8.8.``` Below, we'll explore the components and concepts involved in this infrastructure design.

## To access the designs:
```
- Open a file
- copy the image link and paste it on your browser search bar and press enter
```

### Server
A server is a computer system or software that provides functionality for other programs or devices, known as clients.

### Domain Name
A domain name is a human-readable label that is used to identify a website. It serves as an easy-to-remember alias for the website's IP address.

### DNS Record
The "www" in www.foobar.com is a subdomain, and it typically corresponds to a DNS record type called a CNAME (Canonical Name) record.

### Web Server
The web server's role is to handle HTTP requests from clients (such as web browsers) and deliver web content (HTML pages, images, etc.) in response.

### Application Server
An application server hosts and manages the software applications and services required to deliver dynamic content to users.

### Database
The database stores and manages the website's data, such as user information, content, and configuration settings.

### Communication with User's Computer
The server communicates with the user's computer over the Internet using protocols such as HTTP or HTTPS.

### Load Balancer
A load balancer distributes incoming network traffic across multiple servers to ensure efficient utilization of resources. **Our load balancer is configured with a round-robin distribution algorithm.**

### Active-Active vs. Active-Passive Setup
Our load balancer is configured for an **Active-Passive setup**, where one server (Active) handles incoming traffic while the other (Passive) remains on standby. In Active-Active, both servers actively handle traffic simultaneously.

### Database Primary-Replica Cluster
This setup involves a primary database node (Master) and one or more replica nodes (Slaves). The primary node handles write operations, while replica nodes replicate data from the primary node for read operations.

### Difference between Primary and Replica Nodes
The primary node handles write operations and serves as the authoritative source of data. Replica nodes replicate data from the primary node and serve read requests, providing scalability and fault tolerance.

### Firewalls
Firewalls are security devices or software that monitor and control incoming and outgoing network traffic, based on predetermined security rules.

### HTTPS
HTTPS encrypts the data transmitted between the server and the client, enhancing security and protecting sensitive information from interception or tampering.

### Monitoring
Monitoring tools are used to track the performance, availability, and security of the web infrastructure. They collect data such as server metrics, error logs, and user activity.

### Data Collection by Monitoring Tool
The monitoring tool collects data through various methods, including agent-based monitoring, log scraping, and API integrations with server software.

### Monitoring Web Server QPS
To monitor the web server's Queries Per Second (QPS), configure the monitoring tool to track incoming HTTP requests and calculate the average QPS over a specific time period.

## Conclusion
This readme provides an overview of the web infrastructure design and the roles of its components.

[@Iganza-roy](https://github.com/Iganza-roy)
