#!/usr/bin/env python3
# Foundations of Python Network Programming - Chapter 4 - dns_mx.py
# Looking up a mail domain - the part of an email address after the `@`
import sys
import dns.resolver

if len(sys.argv) != 2:
    print('usage: dns_basic.py <hostname>', file=sys.stderr)
    sys.exit(2)

def resolve_hostname(hostname, indent=0):
    """Print an A or AAAA record for `hostname`; follow CNAMEs if necessary."""
    indent += 4
    istr = ' ' * indent

    try:
        answers = dns.resolver.resolve(hostname, 'A')
        for answer in answers:
            print(istr, 'Hostname', hostname, '= A', answer.to_text())
        return
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
        pass

    try:
        answers = dns.resolver.resolve(hostname, 'AAAA')
        for answer in answers:
            print(istr, 'Hostname', hostname, '= AAAA', answer.to_text())
        return
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
        pass

    try:
        answers = dns.resolver.resolve(hostname, 'CNAME')
        for answer in answers:
            cname = answer.to_text()
            print(istr, 'Hostname', hostname, 'is an alias for', cname)
            resolve_hostname(cname, indent)
        return
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
        pass

    print(istr, 'ERROR: no records for', hostname)

def resolve_email_domain(domain):
    """Print mail server IP addresses for an email address @ `domain`."""
    try:
        answers = dns.resolver.resolve(domain, 'MX')
        print('The domain %r has explicit MX records!' % (domain,))
        print('Try the servers in this order:')
        datalist = sorted((answer.preference, answer.exchange.to_text()) for answer in answers)
        for priority, hostname in datalist:
            print('Priority:', priority, ' Hostname:', hostname)
            resolve_hostname(hostname)
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
        print('Drat, this domain has no explicit MX records')
        print('We will have to try resolving it as an A, AAAA, or CNAME')
        resolve_hostname(domain)

resolve_email_domain(sys.argv[1])


