import unittest
import os
import sys
from time import sleep

from mozprocess import killableprocess
from mozprocess import processhandler

class ProcTest1(unittest.TestCase):

    def startchrome(self):
        CHROMEPATH = ["C:\\Users\\ctalbert\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe"]
        args = ["http://www.mozilla.org", "http://www.wikipedia.org"]
        cmd = CHROMEPATH + args
        kp_kwargs = {}
        p = killableprocess.runCommand(cmd, env = os.environ, **kp_kwargs)
        return p

    def startffx(self):
        FFXPATH = ["C:\\Program Files (x86)\\Minefield\\firefox.exe"]
        args = ["--no-remote", "http://youtube.com"]
        cmd = FFXPATH + args
        kp_kwargs = {}
        p = killableprocess.runCommand(cmd, env = os.environ, **kp_kwargs)
        return p

    def prochandlerstartffx(self):
        FFXDIR = "C:\\Program Files (x86)\\Minefield"
        args = ["--no-remote", "http://youtube.com"]
        p = processhandler.ProcessHandler("C:\\Program Files (x86)\\Minefield\\firefox.exe", args, FFXDIR)
        return p
    def starttestprg(self):
        WORKDIR = "C:\\Users\\ctalbert\\projects\\processlauncher\\processlauncher\\Debug"
        args = []
        p = processhandler.ProcessHandler("C:\\Users\\ctalbert\\projects\\processlauncher\\processlauncher\\Debug\\processlauncher.exe", args, WORKDIR)
        return p
        
#    def test_multiprockill(self):
        #p = self.startchrome()
#        p = self.startffx()
#        sleep(60)
#        p.kill()

#    def test_multiwaittimeout(self):
#        print "STARTING WAIT TEST"
#        #p = self.startchrome()
#        p = self.startffx()
#        p.wait(timeout=60)
     
    def test_prochandler_kill(self):
        #p = self.prochandlerstartffx()
        p = self.starttestprg()
        p.run()
        sleep(25)
        rc = p.kill()
        print "got rc back as : %s" % rc

    def test_prochandler_wait(self):
        p = self.starttestprg()
        p.run()
        rc = p.waitForFinish()
        print "wait: got rc: %s" % rc
