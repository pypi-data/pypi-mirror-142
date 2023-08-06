# Useragent_classifier

## Installation 

```
pip install useragent_classifier
```

## Basic Usage

### Text
```
useragent_classifier -f /tmp/mylist_of_User_agent.csv
```

Where mylist_of_User_agent.csv file is in the following format, one user agent by row, with no header
|                                                                          |
|--------------------------------------------------------------------------|
| Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko     |
| Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0 |
| Opera/6.11 (Linux 2.4.18-bf2.4 i686; U)  [en]                            |

It will produce a two files:
- a file with cluster number attributed to each User agent
- a file usefull to explain cluster with the most important word or set of word in this cluster

### Graphical analysis of cluster    

```
useragent_classifier -f /tmp/mylist_of_User_agent.csv --graphical-explanation
```

Launch a graphical analysis of cluster on local host on port 8050

![Alt text](ressources/example_dashboard.png?raw=true "Screenshot dashboard")


## More advanced Usage

To display the help
```
useragent_classifier --help
```

