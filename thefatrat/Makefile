PORTNAME=	thefatrat
DISTVERSION=	813.b0586d0
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Easy tool to generate backdoor and easy tool to post exploitation attack.
WWW=		https://github.com/Screetsec/TheFatRat

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/android-apktool \
		??/android-sdk-build-tools \
		??/apache \
		??/backdoor-factory \
		??/bind-tools \
		??/dex2jar \
		??/exploitdb \
		??/gcc \
		??/gnome-terminal \
		??/imagemagick \
		??/jdk8-openjdk \
		??/jre8-openjdk \
		??/lib32-zlib \
		??/lsb-release \
		??/metasploit \
		??/mingw-w64-gcc \
		??/mono \
		??/ncurses \
		??/py-names@${PY_FLAVOR} \
		??/ruby-nokogiri \
		??/smali \
		??/sudo \
		??/upx \
		??/xterm \
		archivers/unzip \
		lang/python \
		lang/python3 \
		security/openssl


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
