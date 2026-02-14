PORTNAME=	xcavator
DISTVERSION=	5.bd9e2d8
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Man-In-The-Middle and phishing attack tool that steals the victims credentials of some web services like Facebook.
WWW=		https://github.com/nccgroup/xcavator

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-configparser@${PY_FLAVOR} \
		??/py-ipaddr@${PY_FLAVOR} \
		??/py-ipaddress@${PY_FLAVOR} \
		??/py-pysmb@${PY_FLAVOR} \
		??/py-pysmbc@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
