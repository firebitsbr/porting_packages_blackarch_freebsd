PORTNAME=	opendoor
DISTVERSION=	v.4.2.0.r4.g5f8a253
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	OWASP WEB Directory Scanner.
WWW=		https://github.com/stanislav-web/OpenDoor

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-ddt@${PY_FLAVOR} \
		??/py-json2html@${PY_FLAVOR} \
		??/py-mock@${PY_FLAVOR} \
		??/py-tabulate@${PY_FLAVOR} \
		??/py-urllib3@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
