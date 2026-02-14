PORTNAME=	sharesniffer
DISTVERSION=	v0.1.b.8.r8.ga0c5ed6
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Network share sniffer and auto-mounter for crawling remote file systems.
WWW=		https://github.com/shirosaidev/sharesniffer

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-netifaces@${PY_FLAVOR} \
		??/py-nmap@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
