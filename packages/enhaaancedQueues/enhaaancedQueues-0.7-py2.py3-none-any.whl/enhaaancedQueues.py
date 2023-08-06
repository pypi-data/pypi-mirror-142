#!/usr/bin/python
# -*- coding: utf-8 -*-


# EnhaaancedQueues - Copyright & Contact Notice
###############################################
# Created by Dominik Niedenzu                 #      
# Copyright (C) 2022 Dominik Niedenzu         #       
#     All Rights Reserved                     #
#                                             #
#           Contact:                          #
#      pyadaaah@blackward.de                  # 
#      www.blackward.de                       #         
###############################################


# EnhaaancedQueues - Version & Modification Notice
##################################################
# Based on EnhaaancedQueues Version 0.70         #
# Modified by --- (date: ---)                    #
##################################################


# EnhaaancedQueues - License
#######################################################################################################################
# Use and redistribution in source and binary forms, without or with modification,                                    #
# are permitted (free of charge) provided that the following conditions are met (including the disclaimer):           #
#                                                                                                                     #
# 1. Redistributions of source code must retain the above copyright & contact notice and                              #
#    this license text (including the permission notice, this list of conditions and the following disclaimer).       #
#                                                                                                                     #
#    a) If said source code is redistributed unmodified, the belonging file name must be enhaaancedQueues.py and      #
#       said file must retain the above version & modification notice too.                                            #
#                                                                                                                     #
#    b) Whereas if said source code is redistributed modified (this includes redistributions of                       #
#       substantial portions of the source code), the belonging file name(s) must be enhaaancedQueues_modified*.py    #
#       (where the asterisk stands for an arbitrary intermediate string) and said files                               #
#       must contain the above version & modification notice too - updated with the name(s) of the change             #
#       maker(s) as well as the date(s) of the modification(s).                                                       #
#                                                                                                                     #
# 2. Redistributions in binary form must reproduce the above copyright & contact notice and                           #
#    this license text (including the permission notice, this list of conditions and the following disclaimer).       #
#    They must also reproduce a version & modification notice similar to the one above - in the                       #
#    sense of 1. a) resp. b).                                                                                         #
#                                                                                                                     #
# 3. Neither the name "Dominik Niedenzu", nor the name resp. trademark "Blackward", nor the names of authors resp.    #
#    contributors resp. change makers may be used to endorse or promote products derived from this software without   #
#    specific prior written permission.                                                                               #
#                                                                                                                     #
# THIS SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO   # 
# THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.                            #
#                                                                                                                     #
# IN NO EVENT SHALL DOMINIK NIEDENZU OR AUTHORS OR CONTRIBUTORS OR CHANGE MAKERS BE LIABLE FOR ANY CLAIM, ANY         # 
# (DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY OR CONSEQUENTIAL) DAMAGE OR ANY OTHER LIABILITY, WHETHER IN AN    #
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THIS SOFTWARE (OR PARTS OF THIS   #
# SOFTWARE) OR THE USE OR REDISTRIBUTION OR OTHER DEALINGS IN THIS SOFTWARE (OR PARTS OF THIS SOFTWARE).              #
#                                                                                                                     #
# THE USERS RESP. REDISTRIBUTORS OF THIS SOFTWARE (OR PARTS OF THIS SOFTWARE) ARE SOLELY RESPONSIBLE FOR ENSURING     #
# THAT AFOREMENTIONED CONDITIONS ALL ARE MET AND COMPLIANT WITH THE LAW IN THE RESPECTIVE JURISDICTION - BEFORE (!)   #
# THEY USE RESP. REDISTRIBUTE.                                                                                        #
#######################################################################################################################


#import from common libraries
from multiprocessing              import Lock          as Multiprocessing_Lock
from multiprocessing.sharedctypes import RawValue      as Multiprocessing_RawValue
from multiprocessing.queues       import JoinableQueue as Multiprocessing_JoinableQueue
from Queue                        import Empty         as Queue_Empty
from Queue                        import Full          as Queue_Full
from time                         import time          as Time_time
from time                         import sleep         as Time_sleep


#import from own libraries
from enhaaancedLists              import EnhList



#corrected multiprocessing queue
class EnhQueue(Multiprocessing_JoinableQueue):
      """
          The 'EnhQueue' class is inherited from multiprocessing.queues.JoinableQueue -
          which then is enhanced to work properly on all desktop platforms 
          ('Windows', 'macOS' and 'Linux').
          
          Windows:
          ========
          
          Windows processes do not share memory, which means, shared objects
          have to be pickled and transmitted to the respective subprocess 
          via pipe - when given as parameters to (multiprocessing) process calls.
          The 'EnhQueue' class has been made pickable (have a look at it's 
          '__reduce__' method).
          
          macOS:
          ======
          
          The 'qsize' method of the 'multiprocessing.queues.JoinableQueue' does not
          work under some 'macOS'es (and maybe other *nixes); it might lead to a 
          'NotImplementedError'.
          
          The 'EnhQueue' class wraps 'multiprocessing.queues.JoinableQueue' to correct
          this aspect. The additional lock used for that might also have a positive
          effect to the reliability of the methods 'empty' and 'full'.
          
          Miscellaneous:
          ==============

          Shutting down an application with several processes properly is a delicate
          thing, if some of said processes crashed / got stuck. The 'EnhQueue' class
          has been equipped with a semi-blocking 'join' method - a 'join' with a timeout.
          
          Due to the parallel nature of multiprocessing, emptying a queue reliable in
          a setup, where several processes could put another element in said queue during
          or after said emptying is a delicate thing too.
          
          The 'EnhQueue' has been equipped with a 'clear' method emptying the queue in 
          the most reliable and least blocking way possible - as known to the author yet.
          It in particular is designed to be useful during cleaning up when shutting down 
          an application properly.
      """
      
      _lock     = None
      _sizeI    = None
      _maxSizeI = None
      
      
      #constructor
      def __init__(self, maxSizeI=None, mpLock=None, mpRawValue=None ):
          """ 
               If parameter 'maxSizeI' is None, there is no size limitation
               for the queue 'self'.
               
               If parameter 'mpLock' is None, the lock synchronizing the access
               to the internal element counter 'self._sizeI' is automatically
               created and stored in 'self._lock'.
               
               If parameter 'mpRawValue' is None, the 'multiprocessing raw value
               variable' for said internal element counter 'self._sizeI' is
               automatically created and stored in 'self._sizeI'.
          """
          
          #call constructor of parent class
          Multiprocessing_JoinableQueue.__init__(self, maxsize=maxSizeI)
          
          ### create / init shared variables ###
          #lock
          if    mpLock         == None:
                self._lock      = Multiprocessing_Lock()
                
          else:
                self._lock      = mpLock
               
          #size value
          if    mpRawValue     == None: 
                self._sizeI     = Multiprocessing_RawValue("L", 0)
                
          else:
                self._sizeI     = mpRawValue
          
          #init max size
          if    maxSizeI       == None:
                self._maxSizeI  = maxSizeI
                
          else:
                self._maxSizeI  = long(maxSizeI)
                
                
      #pickle overload method
      def __reduce__(self):
          """ 
               Ensures that instances of self are pickable, which means, that they can
               be given as parameters to (multiprocessing) process calls under Windows
               too (Windows processes do not share memory, which means, shared objects
               have to be pickled and then transmitted to the respective subprocess 
               via pipe).
          """
          
          return ( EnhQueue, (self._maxSizeI, self._lock, self._sizeI), self.__getstate__() )
          
          
      #get size
      def qsize(self):
          """ 
               Returns the number of elements in the queue (in 'self').
               
               The returned number of elements might already be outdated then due to
               the nature of multiprocessing.
          """
          
          #get size
          self._lock.acquire(True)
          sizeI = long(self._sizeI.value)
          self._lock.release()
          
          #return size
          return sizeI
          
          
      #check whether empty
      def empty(self):
          """
              Returns True, if the queue is empty.
              
              This information might already be outdated then due to the nature 
              of multiprocessing.
          """
          
          #get size
          self._lock.acquire(True)
          sizeI = long(self._sizeI.value)
          self._lock.release()
          
          #return True or False
          if    sizeI <= 0:
                return True
                
          else:
                return False
                
                
      #check whether full
      def full(self):
          """ 
              Returns True, if the number of elements in the queue 
              is >= 'self._maxSizeI' - if any given.
               
              This information might already be outdated then due to the nature 
              of multiprocessing.
          """
          
          #no max size given
          if self._maxSizeI == None:
             return False
          
          #get size
          self._lock.acquire(True)
          sizeI = long(self._sizeI.value)
          self._lock.release()
          
          #return True or False
          if    sizeI >= self._maxSizeI:
                return True
                
          else:
                return False     
                
                
      #put
      def put(self, obj, block=True, timeout=None):
          """
              Pushes the parameter 'obj' into the queue. Blocks if parameter
              'block' is True - with the timeout 'timeout'.
          """
          
          try:
                 #put
                 Multiprocessing_JoinableQueue.put(self, obj, block, timeout)
                 
                 #inc size
                 self._lock.acquire(True)
                 self._sizeI.value += 1
                 self._lock.release()
            
          except Queue_Full:
                 raise
                 
                 
      #put non-blocking
      def put_nowait(self, obj):
          """ """
          
          self.put(obj, block=False)
          
          
      #get
      def get(self, block=True, timeout=None, taskDone=True):
          """ 
              Pops an element from the queue. Blocks if parameter
              'block' is True - with timeout 'timeout'.
              
              If parameter 'taskDone' is True, the task_done()
              method of the queue automatically is called.
          """
          
          try:
                 #get
                 obj = Multiprocessing_JoinableQueue.get(self, block, timeout)
                 
                 #dec size
                 self._lock.acquire(True)
                 self._sizeI.value -= 1
                 self._lock.release()
                 
                 #check whether task should be acknowledged
                 if taskDone == True:
                    Multiprocessing_JoinableQueue.task_done(self)
                 
                 #return
                 return obj
            
          except Queue_Empty:
                 raise
                            
                 
      #get non-blocking
      def get_nowait(self):
          """ """
          
          self.get(block=False)
          
          
      #clear queue
      def clear(self, retSelFct=lambda el: False, timeoutPerElemF=0.5, timeoutF=2.0):
          """ 
              Clear (empty) queue in the most reliable and least blocking way possible.
              This takes into account, that self.qsize() might be imprecise resp. 
              already outdated - due to the parallel nature of multiprocessing.
              
              Should not be used too often as it might need / block / lock seconds.
              
              This method solely has been developed for being used immediately
              before closing the queue via self.close()! (and free belonging processes)
              
              A list of removed elements for which retSelFct(element) is True, 
              is returned - see code.
          """
          
          #list of elements to be returned - selected by retSelFct
          retL = EnhList()
          
          ### clear queue on basis of self._sizeI.value - semi-blocking ###
          #blocks significantly JUST IF self.qsize() is bigger than the actual number of elements in queue
          try:
                 
                 #delimited emptying-loop
                 self._lock.acquire(True)
                 sizeI = self._sizeI.value
                 self._lock.release()
                 
                 for indexI in range(sizeI):
                     #pop the next element
                     el = self.get( timeout=timeoutPerElemF)
                     if retSelFct(el) == True:
                        retL.push( el )                     
                 
          except Queue_Empty:
                 pass
               
               
          ### clear queue on basis of Queue_Empty exception - non-blocking ###
          #(this is an additional safety measure)
               
          #encourage syncronization - might not be necessary/helpful at all?
          Time_sleep(0.1)
          
          try:
                 startF = Time_time()
                 while (Time_time() - startF) <= timeoutF:
                       el = self.get_nowait()
                       
                       if retSelFct(el) == True:
                          retL.push( el )                     
                       
          except Queue_Empty:
                 pass
               
          #update size
          self._lock.acquire(True)
          self._sizeI.value = 0
          self._lock.release()
          
          #return selected elements - if any
          return retL
       
       
      #join
      def join(self, timeout=None):
          """
              A semi-blocking 'join' method.
          """
          
          with self._cond:
               if not self._unfinished_tasks._semlock._is_zero():
                      self._cond.wait( timeout )
          
      

#TBD: 
#selftest method!
#self._lock.acquire is blocking yet - which might lead to a dead lock in case of a dead process on the other end!?



