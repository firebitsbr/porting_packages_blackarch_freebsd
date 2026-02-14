PORTNAME=	mongoaudit
DISTVERSION=	222.70b83e8
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A powerful MongoDB auditing and pentesting tool .
WWW=		https://github.com/stampery/mongoaudit

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-dnspython@${PY_FLAVOR} \
		??/py-pymongo@${PY_FLAVOR} \
		??/py-urwid@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
