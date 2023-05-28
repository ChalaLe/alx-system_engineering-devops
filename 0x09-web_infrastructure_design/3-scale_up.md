Explanation:

1. User's Computer: Represents the user's device from which they access the website.

2. DNS Resolution: Resolves the domain name www.foobar.com to the IP address
associated with the load balancer.

3. Domain Name + SSL Certificate: The website is configured with a domain name
(www.foobar.com) and an SSL certificate to enable secure communication over HTTPS.

4. Load-Balancer Cluster (HAProxy): The load balancer acts as a central entry
point for incoming requests and distributes them across multiple servers in
the cluster. It ensures scalability, high availability, and efficient
utilization of resources.

5. Web Server: Handles static content delivery, serving files and resources
to the users' browsers.

6. Application Server: Processes dynamic content, executes the application's logic,
and generates responses based on user requests.

7. Database Server: Stores and manages the website's data, providing persistent
storage and retrieval capabilities.

Additional elements and their purposes:

Load-Balancer Cluster: By adding a load-balancer cluster with HAProxy,
we ensure scalability and high availability. It distributes incoming requests
across multiple servers, allowing for efficient handling of traffic and
redundancy in case of server failures.

Splitting Components: Separating the web server, application server, and
database onto their own servers provides isolation and scalability.
It allows each component to scale independently based on the specific
demands of the application.

Importance of Load-Balancer Cluster:

Scalability: The load balancer distributes incoming requests across multiple servers,
allowing for horizontal scaling by adding or removing servers from the cluster based on
traffic demands. It ensures that the website can handle increased traffic and provide
a consistent user experience.

High Availability: The load balancer cluster improves availability by distributing requests
to multiple servers. If one server fails, the load balancer redirects traffic to the
remaining active servers, minimizing downtime and providing a seamless experience for users.

Overall, this infrastructure design addresses the requirements by introducing
a load balancer cluster to handle incoming traffic and distributing requests to multiple servers.
Each server focuses on a specific component, enabling scalability and separation of concerns.
