PORTNAME=	socialpwned
DISTVERSION=	v2.0.1.r7.g333d759
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	OSINT tool that allows to get the emails, from a target, published in social networks.
WWW=		https://github.com/MrTuxx/SocialPwned

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-beautifultable@${PY_FLAVOR} \
		??/py-bs4@${PY_FLAVOR} \
		??/py-chromedriver-autoinstaller@${PY_FLAVOR} \
		??/py-colorama@${PY_FLAVOR} \
		??/py-dateutil@${PY_FLAVOR} \
		??/py-geopy@${PY_FLAVOR} \
		??/py-httpx@${PY_FLAVOR} \
		??/py-imagehash@${PY_FLAVOR} \
		??/py-moviepy@${PY_FLAVOR} \
		??/py-pillow@${PY_FLAVOR} \
		??/py-pysocks@${PY_FLAVOR} \
		??/py-requests-toolbelt@${PY_FLAVOR} \
		??/py-selenium-wire@${PY_FLAVOR} \
		??/py-selenium@${PY_FLAVOR} \
		??/py-termcolor@${PY_FLAVOR} \
		??/py-wayback@${PY_FLAVOR} \
		??/scrapy \
		??/twint \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
