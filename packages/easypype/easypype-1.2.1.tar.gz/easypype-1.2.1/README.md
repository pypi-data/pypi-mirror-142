# EasyPype - Create flexible, extensible, potent pipelines
EasyPype offers you a simple way to orchestrate a set of operations in a specific order.


## Table of contents
* [Overview](#overview)
* [Why](#why)
* [How](#how)
* [Quickstart](#quickstart)
* [Modules](#modules)


## Overview
EasyPype will offer you:

  - Easy and flexible way to define a set of operations and the correct order to execute them.
  - Multiprocessing execution of your operations.
  - Extensible code, so you can add new features easily.

## Why
Sometimes, you want to orchestrate complex operations, performed by different entities, in a specific order. For instance, take a look at a data pipeline. It's basically a set of nodes doing operations, following the defined flux. Although the data pipeline is a good example, there are many others.

Therefore, the orchestration problem exists in different contexts. So, It would be nice to have some anticipated solution, because the problem repeats itself. That's easypype.

## How
In order to orchestrate complex operations, this solution considers two main entities: Commands and Pipe. A Command is the operation you want to perform and the Pipe is the orchestrator. Hence, the Pipe entity contains a list of Commands to be executed.

Also, all Commands must be able to know the state of the execution. Then, the Sink entity was created and It holds the state over all executions, until the Pipe ends It's job.

In an effort to implement these ideias, two design patterns were used: Command and Builder. The first one allows the Pipe to orchestrate things and the second will help specifying which operations (and what order) to execute.

## Quickstart
First, you must install EasyPype:
```
pip install easypype
```

Then, create a new python file and import it:
```
import easypype as ep
```

To understand how EasyPype will help you, let's take a look at this code snippet:
```
import easypype as ep

pipe = ep.PipeBuilderConcrete().command(ep.Sum(2)).build()
mySink = ep.ConcreteSink()
mySink.collect([1, 2, 3])
pipe.do(mySink)
```

EasyPype uses four modules:
1. "command", has the Command class, the generic pipe operation.
2. "pipe", holds classes related to pipe logic: Pipe, a command that executes a given list of commands, and PipeBuilder, the entity responsible to create a Pipe object. 
3. "sink", knows the Sink class, a basic data holder.
4. "log", gives you a configured logger using "logging" from python.
    
Hence, you can:
- Load data
```
mySink = ep.ConcreteSink()
mySink.collect([1, 2, 3])
```
- Setup operations
```
pipe = ep.PipeBuilderConcrete().command(ep.Sum(2)).build()
```
- Run pipeline
```
pipe.do(mySink)
```

### Adding custom commands
By default, EasyPype has a command called Sum that iterates an iterable object and increases each register by some amount. However, you can easily define your command:
```
import easypype as ep

class Multiplier(ep.Command):

    def __init__(self, amount):
        self.amount = amount

    def multiply(self, sink: ep.Sink):
        return [i * self.amount for i in sink.data]

    def do(self, sink: ep.Sink):
        return self.multiply(sink)
        
pipe = ep.PipeBuilderConcrete().command(Multiplier(2)).build()
mySink = ep.ConcreteSink()
mySink.collect([1, 2, 3])
pipe.do(mySink)
print(mySink.data)
```

Commands **need** four things to work:
1. Extends Command class.
2. Implement do(self, sink: ep.Sink).
3. Return the data after the operation is completed.

Keep in mind that the Sink will collect all returned values by the Command.


## Modules
* [command](#command)
* [pipe](#pipe)
* [sink](#sink)

### command
- Command: interface that declares how a command should be implemented.<br/>
=> do(self, sink: Sink):
 executes the Command and returns new data.<br/>
=> \__init__(self, args*):
 gets command parameters.<br/>
- Sum: command that increases each register of an iterable by some value.<br/>
=> \__init__(self, amount: Number):
 gets the value to be summed.
 
### pipe
- Pipe: special command that executes a list of other commands.<br/>
=> do(self, sink: Sink):
 executes each command listed internally.<br/>
- PipeBuilder: interface that declares how a pipe builder should be implemented.<br/>
=> build(self) -> Pipe:
 returns the built Pipe.<br/>
=> command(self, command: Command):
 append command to the Pipe command list.<br/>
- PipeBuilderConcrete: PipeBuilder implementation.

### sink
- Sink: interface that declares how a sink should be implemented.<br/>
=> data(self):
 property that returns data inside the Sink.<br/>
=> collect(self, data: Any):
 data property setter.<br/>
- ConcreteSink: Sink implementation.<br/>
