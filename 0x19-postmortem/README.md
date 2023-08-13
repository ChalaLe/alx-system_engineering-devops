
**Issue Summary**

The outage occurred on August 5th, 2023, from 10:00 AM to 12:30 PM (UTC+0). During this period, the user authentication 
service experienced an outage, resulting in users being unable to log in to the platform. Approximately 20% of users 
were affected, resulting in a significant degradation of user experience.
**Timeline**

* 10:00 AM: Issue detected by monitoring system alerting unusually high error rates in the authentication service.
* 10:10 AM: Engineering team was notified automatically through the on-call rotation.
* 10:15 AM: Initial investigation focused on the database cluster as a possible cause of the issue.
* 10:30 AM: Engineers discovered that the database was running smoothly, ruling out the initial   assumption.
* 10:45 AM: Investigation shifted towards network issues between the authentication service and the database.
* 11:00 AM: Engineers discovered a network misconfiguration causing packet loss between the two services.
* 11:15 AM: The incident was escalated to the DevOps team to resolve the network misconfiguration.
* 12:00 PM: The DevOps team identified the root cause as a misconfigured firewall rule blocking the necessary network traffic.
* 12:15 PM: The firewall rule was adjusted to allow the required traffic to pass through.
* 12:30 PM: User authentication service was restored, and error rates normalized.
**Root Cause and Resolution**
  
The root cause of the issue was a misconfigured firewall rule that blocked network traffic between the authentication service
and the database. The firewall rule was inadvertently updated during routine maintenance, leading to packet loss and a 
communication breakdown between the services.

To resolve the issue, the DevOps team quickly identified the misconfigured firewall rule and corrected it. 
Once the necessary network traffic was allowed to flow between the authentication service and the database,
the services were able to communicate properly, and the user authentication functionality was restored.
**Corrective and Preventative Measures**

To prevent similar incidents in the future, the following corrective and preventative measures have been implemented:
* Regular auditing of firewall rules and network configurations to ensure consistency and accuracy.
* Introduction of automated network configuration tests to detect potential misconfigurations early.
* Enhanced monitoring of network traffic and error rates to quickly identify abnormalities.
* Implementation of automated backups for network configuration settings to facilitate rapid restoration in case of accidental changes.
**Tasks to Address the Issue**

*1.	Conduct a comprehensive review of firewall rules and document dependencies between services.
*2.	Develop and implement a network configuration testing script to run regularly.
*3.	Enhance monitoring system to provide more detailed insights into network traffic patterns.
*4.	Establish automated network configuration backups to safeguard against accidental changes.

In conclusion, the outage was caused by a misconfigured firewall rule that disrupted communication between the user 
authentication service and the database. Through diligent investigation and quick action, the issue was resolved, 
and measures have been taken to prevent similar incidents in the future. The incident underscored the importance of 
robust network configuration management and proactive monitoring to ensure the reliability and availability of critical services.
