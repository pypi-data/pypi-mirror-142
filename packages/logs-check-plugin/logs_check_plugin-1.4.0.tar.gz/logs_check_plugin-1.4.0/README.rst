Logs monitoring plugin
===========================

Checks an url raise an alert if some problem is found.
Uses curl with all its power, so you can extend your check with all curl options.

`VERSION  <logs_check/VERSION>`__

Install
=======

Linux::

    sudo pip3 install logs_plugin --upgrade

Also is possible to use::

    sudo python3 -m pip install logs_plugin --upgrade

On windows with python3.5::

    pip install logs_plugin --upgrade

For proxies add::

    --proxy='http://user:passw@server:port'

Usage
=====

Use the command line::

    > logs_plugin --help
      usage: logs_plugin [-h] [-fl [Fileocation]] [-wd [Word to Check]] [-e [EXTRA_ARGS]] 

        optional arguments:
                            -h, --help            show this help message and exit
                            -fl [Fileocation], --filelocation [Fileocation]
                                                    file to check
                            -wd [Word_to_check], --wordtocheck [Word to Check]
                                                    word to check
                            -e [EXTRA_ARGS], --extra_args [EXTRA_ARGS]
                                                    extra args to add to curl, see curl manpage


Example usage
=============

Example basic usage::

    > logs_plugin  --fl '{filelocation}' --wd '{word_to_check}'

Nagios config
=============

Example command::

    define command{
        command_name  logs_plugin
        command_line  /usr/local/bin/logs_plugin --fl '$ARG1$' --wd $ARG2$ $ARG3$ 
    } 

With proxy defined

# use logs_plugin with proxy

    define command {
        command_name  logs_plugin
        command_line  https_proxy=http://user:pass@PROXYIP:PORT /usr/local/bin/logs_plugin --fl '$ARG1$' --wd $ARG2$  $ARG5$}

Example service::

    define service {
            host_name                       SERVERX
            service_description             service_name
            check_command                   logs_plugin!c:\logs\log.txt!wordtocheck
            use				                generic-service
            notes                           some useful notes
    }
    
With proxy defined:

    define service {
            host_name                       SERVERX
            service_description             service_name
            check_command                   logs_plugin!c:\logs\log.txt!wordtocheck
            use				                generic-service
            notes                           some useful notes} 

You can use ansible role that already has the installation and command: https://github.com/CoffeeITWorks/ansible_nagios4_server_plugins

TODO
====

* Use hash passwords
* Add Unit tests?
