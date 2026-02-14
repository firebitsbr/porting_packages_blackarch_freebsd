PORTNAME=	cmsscan
DISTVERSION=	43.f060b4b
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	CMS scanner to identify and find vulnerabilities for Wordpress, Drupal, Joomla, vBulletin.
WWW=		https://github.com/ajinabraham/CMSScan

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/droopescan \
		??/gunicorn \
		??/joomscan \
		??/py-fake-useragent@${PY_FLAVOR} \
		??/py-flask-basicauth@${PY_FLAVOR} \
		??/py-flask@${PY_FLAVOR} \
		??/vbscan \
		??/wpscan \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
