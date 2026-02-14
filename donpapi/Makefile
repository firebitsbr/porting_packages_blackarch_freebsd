PORTNAME=	donpapi
DISTVERSION=	V1.2.0.r40.g61db37a
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Dumping revelant information on compromised targets without AV detection with DPAPI.
WWW=		https://github.com/login-securite/DonPAPI

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		devel/git \
		devel/py-pip@${PY_FLAVOR}

RUN_DEPENDS=	??/exrex \
		??/impacket-ba \
		??/py-dploot@${PY_FLAVOR} \
		??/py-flask-basicauth@${PY_FLAVOR} \
		??/py-flask-cors@${PY_FLAVOR} \
		??/py-flask-rich@${PY_FLAVOR} \
		??/py-flask@${PY_FLAVOR} \
		??/py-jinja@${PY_FLAVOR} \
		??/py-marshmallow-sqlalchemy@${PY_FLAVOR} \
		??/py-pyjwt@${PY_FLAVOR} \
		??/py-rich@${PY_FLAVOR} \
		??/py-sqlalchemy@${PY_FLAVOR} \
		??/py-termcolor@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
