PORTNAME=	droopescan
DISTVERSION=	1.45.1
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A plugin-based scanner that aids security researchers in identifying issues with several CMSs, mainly Drupal & Silverstripe.
WWW=		https://github.com/droope/droopescan

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-cement@${PY_FLAVOR} \
		??/py-dateutil@${PY_FLAVOR} \
		??/py-lxml@${PY_FLAVOR} \
		??/py-mock@${PY_FLAVOR} \
		??/py-nose@${PY_FLAVOR} \
		??/py-pystache@${PY_FLAVOR} \
		??/py-simplejson@${PY_FLAVOR} \
		??/py-twisted@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
