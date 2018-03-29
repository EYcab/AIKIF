#!/usr/bin/python3
# coding: utf-8
# comms.py

import datetime

import cls_log as mod_log
import config as mod_cfg


lg = mod_log.Log(mod_cfg.fldrs['log_folder'])
lg.record_process('comms.py', 'Initialing Comms...')


class CommsManager(object):
    """
    overall manager to handle all channels
    """
    def __init__(self):
        self.channels = []

    def __str__(self):
        res = ' /---- CommsManager -------------------------- \n'
        for c in self.channels:
            res += '|  channel : ' + str(c) + '\n'
        res += '\---------------------------------------------\n'
        return res


    def add_channel(self, channel, pwd_hash):
        """
        adds a channel, but must have authenication
        """
        if channel.pwd_hash == pwd_hash:
            self.channels.append(channel)
            lg.record_process('comms.py', 'Added channel ' + channel.name)

            return True
        else:
            lg.record_process('comms.py', 'ERROR - Cant add channel : wrong hash for ' + channel.name)
            return False

    def delete_channel(self, channel, pwd_hash):
        """
        adds a channel, but must have authenication
        """
        if channel.pwd_hash == pwd_hash:
            self.channels.remove(channel)
            lg.record_process('comms.py', 'Removed channel ' + channel.name)

            return True
        else:
            lg.record_process('comms.py', 'ERROR - Cant delete : wrong hash for  ' + channel.name)
            return False





class Channel(object):
    """
    handles a single channel like audio input, output, sensors
    """
    def __init__(self, name, pwd_hash):
        self.name = name
        self.pwd_hash = pwd_hash
        self.inc_msg = 0



    def __str__(self):
        res = self.name
        res += ' : ' + str(self.inc_msg) + ' incoming messages'
        return res


class Message(object):
    """
    handles a message
    """
    def __init__(self, sender, receiver, title, details):
        self.sender = sender
        self.receiver = receiver
        self.title = title
        self.details = details
        self.date_msg = datetime.datetime.now()
        self.send_success = False

    def __str__(self):
        res = self.name
        res += ' : ' + str(self.sender) + ' attempting to send message to ' + str(self.receiver)
        return res


    def send(self):
        """
        this handles the message transmission
        """
        print('sending message to ' + self.receiver)

        ## TODO - send message via library

        return True 
