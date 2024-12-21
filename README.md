# MOF

MOF is the Meta Operator Framework.

Many configuration management solutions exist, such as Puppet, Kubernetes, Terraform, and others.

In the end, most of those configuration management solutions are about a declarative description of a configuration and a mechanism for applying the configuration.

Additionally, many of those solutions have:

* Remote execution capabilities
* Orchestration capabilities

The MOF intends to provide a generic interface to build configuration management solutions in a way that can integrate with existing configuration management solutions.

## Operators

The MOF is based around the concept of an operator.

An operator is an executable command that follows a standardized command-line interface.

For example, the `operators` directory contains sample operators.
`python/files-operator` can render files using Jinja templates.
With `input.yaml`:

```
files:
  /tmp/example: |
    # example
    Foo: {{ foo }}
    Bar: {{ bar }}
variables:
  foo: qux
```

and `secrets.json`:

```
{"bar": "secret bar"}
```

then:

```
$ files-operator input.yaml --secrets secrets.json
```

Creates `/tmp/example` with contents:

```
# example
Foo: qux
Bar: secret bar
```

### Specification

#### `input`

The `input` argument is the path to the input data file.
The input data file contains the description of the configuration that the operator applies.

#### `--secrets`

The `--secrets` argument is an optional path to a secrets data file.
Operators can read values from secrets data.

Operators should treat values from secrets data as sensitive information.
For example, operator output should always mask secret data.

#### Data file

A data file is a file that contains JSON-like information in any supported format, such as JSON, YAML, etc.
