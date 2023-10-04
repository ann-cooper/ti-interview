# Summary
This assignment aims to evaluate your technical skills.
Please try to complete this assignment as much as you can prior to your full-loop interview. You can spend as much or as little time on this assignment as you feel is appropriate. Remember your goal is to showcase your general technical abilities and be able to talk about your solutions during the code review portion of the interview.

## Assignment
### 1. Write a function to find nth fibonacci number.
- [Answer](nth_fibonacci.py) has an example using iteration and one using recursion.

### 2. Implement polymorphic function for movement for animals (kangaroo, cat, snake).
- [Answer](animals.py) can also be run in a shell with `python animals.py`

### 3. Implement two Classes that make use of inheritance.
- The answer to question 2 uses inheritance, but another example is [here](inheritance.py).  
a. Describe closure.
    - A closure is when a function retains access to variables in the enclosing scope. The place that I have most often seen closures in Python is in decorators. [Here are examples of a closure and a decorator](closures.py).

### 4. Explain the “Chain of Responsibility” Design Pattern as it could apply to #2 above? If it doesn’t apply, explain why not.
- The Chain of Responsibility pattern is a behavioral pattern meant to allow handlers to be decoupled from the objects they handle. An object could be handled by multiple handlers and the handlers take care figuring out if they can process the object or if they need to pass it along to the next handler.

- The Chain of Responsibility pattern isn't one that I have run into a lot working in Python, but I wrote an example of the Chain of Responsibility [here](inheritance.py) along with a different version that does the same thing. The alternative class, AnotherFileHandler, loses the decoupling of Chain of Responsibility because both file types are handled in one 'process' method instead of independent handler classes. On the other hand, it gains greater clarity, it's easier to read and reson about, and because of that it would be easier to maintain.

- As a side note, Python is an interesting case, because in some instances, features of the language mean that some of the design patterns that a language like Java might need are unnecessary (or just clunky) in Python. This isn't to say that design patterns aren't useful in Python, because many are! My favorite references for this relationship between Python and design patterns are [this Pycon Australia talk](https://2018.pycon-au.org/talks/45184-you-dont-need-that/) and this [Python Design Patterns](https://python-patterns.guide/) site. 

### 5. Describe slowly changing dimensions.  
Slowly changing dimensions allow data warehouses to capture changes to dimensional attributes. Overwriting, adding a row to reflect the new value and effective dates, or adding a column so that both the current and previous values are stored (SCD types 1, 2, and 3) are the most common approaches.

a. How does type 6 work?

- SCD type 6 uses concepts from SCD 1, SCD 2, and SCD 3.
- SCD 3&1: The old row gets a new column for the current value, and the column value is overwritten with the current value in all of the old rows.
- SCD 2: The new row tracks which row is current and the effective dates.
- Margy Ross describes it this way, "The type 6 moniker was suggested by an HP engineer in 2000 because it’s a type 2 row with a type 3 column that’s overwritten as a type 1." [source](https://www.kimballgroup.com/2013/02/design-tip-152-slowly-changing-dimension-types-0-4-5-6-7/)

b. How does type 2 work?

- SCD type 2 adds a new row when values change, and includes columns that indicate which row is currently valid and dates for when the change went into effect and when it expires.  

### 6. What are the considerations for building data pipelines end-to-end?

Considerations for building a data pipeline can be broken into two broad areas: lifecycle and purpose. Lifecycle considerations include both functional and metadata areas and are further divided into the stages of the data lifecycle and data governance, which hooks into the data lifecycle. Purpose considerations include the audience for the end product of the data pipelines and what uses they have for the data.

#### Lifecycle:

- The data lifecylce and data governance are two different concepts that interact at several points: 
    - Lifecyle stage: Ingest 
        - What are the data sources?
        - How can we pull data from them?
    - Lifecyle stage: Transformation
        - This includes anything that needs to be done to the raw data in order for it to be usable. That can include cleaning, enriching, etc.
        - Governance actions:
            - Quality: Data quality can include many different measures, but some common ones are completeness, uniqueness, and consistency.
            - Lineage: Data lineage means tracing where the data originated and what changed it in the journey from raw to clean.
    - Lifecycle stage: Persistence
        - This includes decisions about where and how to store the data (on prem? cloud?) and any retention policies for archiving or destroying data.
        - Governance actions: 
            - Security: Security at the persistence stage includes things like encryption of data and data localization (laws about where certain kinds of data must be stored).
    - Lifecycle stage: Access
        - Access to the data is related to the data users (the audience) and should cater to their use cases and needs. This might mean using UI data exploration tools and / or providing read access to the clean data.
        - Governance actions: 
            - Access control & ownership: These are separate concerns from security of the data storage. There can be role-based access to certain kinds of data, and to certain kinds of actions on the data. Data ownership is also important to establish so that responsibility for decisions about access and retention are clear.
            - Privacy: does the data contain PII or medical information that needs to be redacted or obscured? Are there regulations like GDPR in play?  

Further considerations about the lifecycle stages:

- Who is handling each part of the data lifecycle?
    - Is there one team that stewards the data, or does each team steward its own data? 
- What tools will be used? 
    - What tools does the team have experience with? 
    - Does the team have the ability to skill up on new tools quickly? This can be influenced not only by skill / experience on the team, but by how much work the team has and when it needs to be delivered.
- What budget is there for paid or managed services?
- Size of data and availability of new data:
    - The size and expected availability of new data will point to which tools are best suited. For example, unless there is a lot of Kafka experience at the company and creating a new topic is already supported and easy, standing up an instance of Kafka to handle a data set that isn't enormous, isn't needed in near-real time, or doesn't have to be accessed by multiple microservices probably isn't worth it.
    - Batch or streaming? This will depend on how the data will be used and the needs of the end users. In my experience, unless streaming is definitely and entirely necessary, batch can often be easier to manage and debug, and depending on what platform and tools are being used, it can also be cheaper.

#### Purpose:  
- What problem is the data pipeline meant to solve? The intended usage of the data that the pipeline is producing will affect key technical decisions about the pipeline's design, such as batch versus streaming, what transformations are needed, what aggregations might be needed, etc.  
    
- Who will be using the data and what questions do they hope to be able to answer? Knowing what kinds of questions the data should be able to answer (which gives the team insight into the kinds of queries that might be run) is important to figure out as early in the process as possible. Of course new questions will arise over time, and careful modeling should be able to support a broader set of queries than those that were originally proposed. It's important to help the data users stay informed about what kinds of questions the data can and can't answer.

- There is overlap between the audience and intended use and some of the lifecycle stages, which is intentional: it's important to design for usage. The audience, or audiences, might have different ways of interacting with the data. Some portion of the audience might prefer dashboards or something like Tableau or PowerBI, whereas another portion might want to read directly from the warehouse (or a data mart off of the warehouse).

### 7. What are some considerations when optimizing a pipeline?
- Data size: How much data is it handling and is it using the right technology for the size?
- Handling new data: How often is the data being ingested and what are the expectations of the users? Do we need streaming or batch?
- Queries: Are we only getting the data we need or are we getting more?
- Transformations: Are we only operating on the data that need to be transformed? Is the code handling the transformations efficient?
- Speed: Is the pipeline producing data as quickly as is needed?
- Scalability: Can the pipeline scale up appropriately for heavier loads?
- Observability: Do we have insight into what went wrong when an error occurs?

7a. How do you use Snowflake to profile a query?  
- Use "query profile" from the detail page for the query. If the query id column is displayed, then the id is clickable and the profile tab can be accessed via the History or Worksheets page. [Reference](https://docs.snowflake.com/en/user-guide/ui-query-profile)

### 8. What are some benefits of using Snowflake as a Data Warehouse?
- Replication across clouds: Snowflake allows an organization to replicate a database across different clouds, meaning that you can replicate a database on AWS to GCP for failover or to share data to a new region.
- Separate scaling: Snowflake allows users to scale compute and storage separately, as opposed to data warehouses like Redshift where scaling means adding both compute and storage. Snowflake also offers automatic scaling.
- Access control: Snowflake's role-based access control is a better user experience since it doesn't need to account for the location of the data, making secure data access easier to implement no matter where the data is stored.

8a. What is a micro-partition?
- A micro-partition is a unit of storage in Snowflake. Data in Snowflake is automatically stored in micro-partitions. Some benefits of this include: not having to manage your own partitions; small partitions support fast query speeds; and micro-partitions use columnar storage, which allows more efficient queries by reducing the workload to find the needed information as compared to row-oriented storage.

### 9. Explain upstream and downstream as it relates to Apache Airflow.
- The upstream task is the one that immediately precedes a task, and the downstream task is the one that follows. [Reference](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/tasks.html)

### SQL Questions

customers table
| id | name| email |
| --- | --- | --- |
| 1 | Doctor Who| doctorwho@timelords.com |
| 2 | Harry Potter | harry@potter.com |
| 3 | Captain Awesome | captain@awesome.com |


orders table
| id | customer_id | item | price |
| --- | --- | --- | --- |
| 1 | 1 | Sonic Screwdriver | 1000 |
| 2 | 2 | High Quality Broomstick | 40 |
| 3 | 1 | TARDIS | 1000000 |


### 11. Write down queries to find out the following data
- Get the name and email of customers who do not have any order.
    - [Answer](no_orders.sql)
- Get the name and email of customers who have more than one order.
    - [Answer](multiple_orders.sql)

### 12. Get the list of employee name and their corresponding manager names
- Note: Below is the dummy data I used in the sqlite db I created for this assessment.
- [Answer](reports_to.sql)
    ```
    employee_name|manager
    Employee Z|Employee Y
    Employee X|Employee W
    Employee Y|Employee X
    ```

| employee_id | employee_name | email | contact | salary | job_id | manager_id | department_id |
| -- | -- | -- | -- | -- | -- | -- | -- |
|1|Employee Z|emp.z@ti.com|||8abab|3|dept A
|2|Employee X|emp.x@ti.com|||7cb|4|dept Ab
|3|Employee Y|emp.y@ti.com|||7acb|2|dept A
|4|Employee W|emp.w@ti.com|||6b||dept Ab


| id | salary | employee_Name |
| -- | -- | -- |
| 1  | 100    | Yash |
| 2  | 200    | Sneha |
| 3  | 300    | Tim |
| 4  | 200    | Karthik |


### 13. List employee names with 2nd highest salary
- [Answer](salary.sql)

### 14. Two of your engineers are having a disagreement about the best way to handle a situation, and both are valid. How do you resolve this situation?  

I would treat this situation as a way to facilitate a conversation with the engineers to help them evaluate their disagreement according to the criteria below. My hope would be that they'd be able to reach some common ground by talking it through and making the best choice for the team, but if they can't come to an agreement after that, I would be the tie-breaker.
- Which is quicker to implement?
    - If the team is on a difficult deadline and at risk of not finishing something, then the faster solution might be better as long as it won't introduce errors or be difficult to maintain.
- Which is easier to maintain?
    - If the team isn't in a time crunch and one option is easier to maintain and / or clearer and easier to understand, then that would be the better option.
- What is the basis of their disagreement? Is one of them leaning on best practices or best use of language features? Is one of them a personal or purely stylistic preference?
    - I prefer solutions that are based on best practices guidance and best usage of language features. If one of the engineers wants to do it a certain way, but can only back that up with a style preference, then that wouldn't carry much weight with me.
- Is either one of the engineers leading the project? 
    - If so, their option would be my choice if both are equally easy to maintain, equally quick to implement, and the preference is based on something substantive.
    
### 15. You notice that one of your engineers seems to enjoy doing other types of work more than their current responsibilities. What would you do?
- It depends on whether they are neglecting their core job duties in order to focus on the enjoyable tasks. If that were the case, then I'd need to treat it as a performance issue. With performance issues, my first step is to talk with the person and make sure I understand where they're coming from and how they understand their job. I'd need to figure out what they think their job duties are, because it may be that they aren't clear on what's expected of them. In that case, they deserve to know what success looks like in their current role.
- If they enjoy other tasks more, but are still fulfilling the expectations of their role, then I'd want to talk with them about their professional goals and get a sense of what they'd ideally like to be doing. If there's a way to get them more time on the tasks they like without leaving the rest of the team in the position of having to take up their slack, then I'd try to find ways to give them opportunities to do more of what they like. That's not always possible, though! And if it's not, then they need to know what kinds of work we can offer them in their role and what we can't.