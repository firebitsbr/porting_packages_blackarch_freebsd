PORTNAME=	pr0cks
DISTVERSION=	3.3b740fa
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	python script setting up a transparent proxy to forward all TCP and DNS traffic through a SOCKS / SOCKS5 or HTTP(CONNECT) proxy using iptables -j REDIRECT target.
WWW=		https://github.com/n1nj4sec/pr0cks

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/iptables \
		??/py-dnslib@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
