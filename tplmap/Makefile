PORTNAME=	tplmap
DISTVERSION=	719.616b0e5
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Automatic Server-Side Template Injection Detection and Exploitation Tool.
WWW=		https://github.com/epinna/tplmap

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-certifi@${PY_FLAVOR} \
		??/py-chardet@${PY_FLAVOR} \
		??/py-flask@${PY_FLAVOR} \
		??/py-idna@${PY_FLAVOR} \
		??/py-urllib3@${PY_FLAVOR} \
		??/py-yaml@${PY_FLAVOR} \
		lang/python3 \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
