PORTNAME=	phonia
DISTVERSION=	593.8ae14ff
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Advanced toolkits to scan phone numbers using only free resources.
WWW=		https://github.com/entynetproject/phonia

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/geckodriver \
		??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-colorama@${PY_FLAVOR} \
		??/py-config@${PY_FLAVOR} \
		??/py-html5lib@${PY_FLAVOR} \
		??/py-phonenumbers@${PY_FLAVOR} \
		??/py-selenium@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
