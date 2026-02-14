PORTNAME=	wpbullet
DISTVERSION=	34.6185112
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A static code analysis for WordPress (and PHP).
WWW=		https://github.com/webarx-security/wpbullet

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-certifi@${PY_FLAVOR} \
		??/py-chardet@${PY_FLAVOR} \
		??/py-colorama@${PY_FLAVOR} \
		??/py-idna@${PY_FLAVOR} \
		??/py-tabulate@${PY_FLAVOR} \
		??/py-terminaltables@${PY_FLAVOR} \
		??/py-urllib3@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
