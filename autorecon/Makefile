PORTNAME=	autorecon
DISTVERSION=	297.e7e98f6
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A multi-threaded network reconnaissance tool which performs automated enumeration of services.
WWW=		https://github.com/Tib3rius/AutoRecon

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/feroxbuster \
		??/impacket \
		??/oscanner \
		??/py-appdirs@${PY_FLAVOR} \
		??/py-colorama@${PY_FLAVOR} \
		??/py-psutil@${PY_FLAVOR} \
		??/py-toml@${PY_FLAVOR} \
		??/py-unidecode@${PY_FLAVOR} \
		??/redis \
		??/tnscmd \
		??/wkhtmltopdf \
		lang/python \
		security/nmap


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
