# Comparing Azure App Service and Azure Virtual Machine

**Azure App Service** is a *platform as a service (PaaS)* cloud service that is provded by Microsoft. Azure App Service is a platform that enables the developer(s) the freedom to not worry about the underlying infrastracture powering the web app. Rather, it gives the opportunity of only focusing on the deployment aspect of the web/app development cycle. The service affords teams of less manpower or even single individual to efficiently manage the development flow by only focusing on developing the code and deploying them rather than how to setup a web/app server.

**Azure Virtual Machine** is an *nfrastracture as a Service (IaaS)* cloud platform provided by Microsoft. This platform leaves the team the responsibilty of managing their own server, virtual environments and other infrastructures needed to get the server up and running. The team has the responsibility of setting up, managing and scalling the server as need arises. Microsoft only takes care of the physical security of the hardware and the entire data center itself. But the responsibility of installing the Operating System, Webserver, Networks, etc.


### Comparing Azure App Service and Azure Virtual Machine

- *Cost:* Azure App Service is often less costly compared to Azure Virtual Machines. However, if you can setup and optimze azure virtual machine proper, it can likewise be cost effective together with its full computing resource and power. Wrong utilization of Azure app service may also incure more cost than virtual machine.
- *Scalability:* Azure virtual machine are more scalable but requires more competence. Azure app service on the other hand is easier to scale with minimum effort. The downside of app service is that it is limited on how much it can scale. Azure virtual machine however can scale up to 500 TB.
- *Availability:* Azure App Service is highly available but not compared to Azure Virtual Machine that has more dedicated resources.
- *Workflow:* Azure app service workflow is actually easier to follow and manage as the process has been automated by Microsoft. Whilst Azure Virtual Machine is more rigorous as the developement team has to take responsibility of such workflows.
- *Preferred Platform:* The preferred platform here is Azure App Service. The reason being that app service is more suitable and cost effective for small web app as the case for this CMS webapp. The time and technicalities reqiured to deploy the web app is very minimal and as such makes it a good choice. Knowing that there will hardly be any need for future scaling of the CMS, app service is therefore, considered a perfect option for deploying the webapp.
- *Justify your choice*

### Changes That Will Influence This Decision

If requirements changes in the future and there becomes need to serve more numbers of people with the CMS, then there will be need to switch to Azure Virtual Machine to cater for those bottleneck issues.