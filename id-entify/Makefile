PORTNAME=	id-entify
DISTVERSION=	34.dd064a5
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Search for information related to a domain: Emails - IP addresses - Domains - Information on WEB technology - Type of Firewall - NS and MX records.
WWW=		https://github.com/BillyV4/ID-entify

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/bind-tools \
		??/dnsenum \
		??/dnsrecon \
		??/fierce \
		??/py-colorama@${PY_FLAVOR} \
		??/theharvester \
		??/tmux \
		??/wafw00f \
		??/whatweb \
		??/whois \
		lang/python3 \
		security/nmap \
		shells/bash


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
