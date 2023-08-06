# hetzner-fireaccess-cleaner

This CLI is to be used with clearing automated access to a Hetzner firewall

## Getting started
`pip install hetzner-fireaccess-cleaner`

### How does it work?
This script is made to be run by an automation, like crontab.
It's looking for the string `auto-expire-[]` where we have a timestamp to when the listed rule should expire in UNIX time.
> Example: auto-expire-[1647127315]

> Remote access for USER - auto-expire-[1647127315]

It uses the default hcloud CLI config file. https://github.com/hetznercloud/cli

How you implement and use this is up to you.

### Usage
```bash
hetzner-fireaccess-cleaner clean [FIREWALL NAME]
```

For more info about available flags, checkout out the help `hetzner-fireaccess-cleaner -h`.


**Examples**

Clean the firewall `firewall-1`
```bash
hetzner-fireaccess-cleaner clean firewall-1
```

Using a different context than the current active
```bash
hetzner-fireaccess-cleaner --context access-project clean remote-firewall
```

### DEMO
```bash
$ hetzner-fireaccess-cleaner clean remote-firewall
No context provided, using default
Rule marked for removal: A rule which is expored auto-expire-[1647127315]
Removing rules
Finished
```

### Contributions
Contributions are welcome.

### Disclaimer

This has not yet been tested a lot and only on a small hetzner account, use with caution.