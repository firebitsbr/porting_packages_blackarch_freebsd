PORTNAME=	jok3r
DISTVERSION=	447.0761996
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Network and Web Pentest Framework.
WWW=		https://github.com/koutto/jok3r

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-ansi2html@${PY_FLAVOR} \
		??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-blessed@${PY_FLAVOR} \
		??/py-cmd2@${PY_FLAVOR} \
		??/py-colorama@${PY_FLAVOR} \
		??/py-colored@${PY_FLAVOR} \
		??/py-colorlog@${PY_FLAVOR} \
		??/py-enlighten@${PY_FLAVOR} \
		??/py-humanfriendly@${PY_FLAVOR} \
		??/py-libnmap@${PY_FLAVOR} \
		??/py-pillow@${PY_FLAVOR} \
		??/py-prettytable@${PY_FLAVOR} \
		??/py-regex@${PY_FLAVOR} \
		??/py-selenium@${PY_FLAVOR} \
		??/py-shodan@${PY_FLAVOR} \
		??/py-sqlalchemy-utils@${PY_FLAVOR} \
		??/py-sqlalchemy@${PY_FLAVOR} \
		??/py-tld@${PY_FLAVOR} \
		??/py-urllib3@${PY_FLAVOR} \
		devel/py-six@${PY_FLAVOR} \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
