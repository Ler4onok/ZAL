class Node:
    def __init__(self, nextNode, prevNode, data):
        self.data = data
        self.nextNode = nextNode
        self.prevNode = prevNode


class LinkedList:
    def __init__(self):
        self.head = None


class Car:
    def __init__(self, identification, name, brand, price, active):
        self.identification = identification
        self.name = name
        self.brand = brand
        self.price = price
        self.active = active


db = LinkedList()


def init(cars):
    for car in cars:
        add( car )


def add(car):
    head = db.head
    new = Node( None, None, car )


    if head == None:
        db.head = new

    elif car.price < head.data.price:
        new.nextNode = db.head
        db.head = new
        new.nextNode.prevNode = new

    else:
        while (head.nextNode != None) and (head.nextNode.data.price <= car.price):
            head = head.nextNode

        new.nextNode = head.nextNode
        head.nextNode = new
        new.prevNode = head
        if head.nextNode is None:
            new.nextNode.prevNode = new




def updateName(identification, name):
    head = db.head
    while (head != None) and (identification != head.data.identification):
        head = head.nextNode #find the needed node
    if head != None:
        head.data.name = name



def updateBrand(identification, brand):
    head = db.head
    while (head != None) and (identification != head.data.identification):
        head = head.nextNode  # find the needed node
    if head != None:
        head.data.brand = brand

def activateCar(identification):
    head = db.head
    while (head != None) and (identification != head.data.identification):
        head = head.nextNode  # find the needed node
    if head != None:
        head.data.active = True


def deactivateCar(identification):
    head = db.head
    while (head != None) and (identification != head.data.identification):
        head = head.nextNode  # find the needed node
    if head != None:
        head.data.active = False

def getDatabaseHead():
    return db.head


def getDatabase():
    return db


def calculateCarPrice():
    price = 0
    head = db.head
    while head != None:
        if head.data.active == True:
            price+=head.data.price
        head = head.nextNode
    return price

def clean():
    db.head = None


